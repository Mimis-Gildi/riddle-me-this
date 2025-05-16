package me.riddle.the.dependencies

import groovy.json.JsonSlurper
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.io.File

private val dependencyBeanLogger by lazy { LoggerFactory.getLogger(LegacyOutdatedDependenciesProcessor::class.java) }

/**
 * Quick and dirty processor for outdated dependencies.
 * It is done because it only takes a minute.
 * The logic is a direct ripoff of the Gervi Héra Vitr task script by rdd13r.
 * Captain should remodel into a clean reusable service;
 * placeholder is here @see me.riddle.the.dependencies.BenManesDependencyModel
 */
open class LegacyOutdatedDependenciesProcessor(val jsonReportFile: File, val classLogger: Logger = dependencyBeanLogger) {

    val depLogLine = "\t {}:{} => [{} --> {}, {}, {}]"
    val depAltLine = "\t (potentially upgradable) {}:{} => [{} --> {}]"
    val depMsgLine = "::warning file=build.gradle.kts::Dependency update available for %s:%s from %s to %s; also %s and %s"
    val depMsgActive = "::warning file=build.gradle.kts::Dependencies have choices to consider"

    /**
     * These dependencies are explicitly managed by MíMíR `fluffle` engine and need not be reported here.
     */
    val restrictedDependencies = listOf(
        "org.gradle.kotlin.kotlin-dsl:org.gradle.kotlin.kotlin-dsl.gradle.plugin",
        "org.jetbrains.kotlin:kotlin-assignment-compiler-plugin-embeddable",
        "org.jetbrains.kotlin:kotlin-bom",
        "org.jetbrains.kotlin:kotlin-compiler-embeddable",
        "org.jetbrains.kotlin:kotlin-reflect",
        "org.jetbrains.kotlin:kotlin-sam-with-receiver-compiler-plugin-embeddable",
        "org.jetbrains.kotlin:kotlin-scripting-compiler-embeddable",
        "org.jetbrains.kotlin:kotlin-stdlib"
    )

    val reportJson: Map<*, *> by lazy(LazyThreadSafetyMode.PUBLICATION) {
        classLogger.info("\t|=> Dependency Processor: Grabbing JSON Report.")
        JsonSlurper().parseText(jsonReportFile.readText()) as Map<*, *>
    }
    val outdatedDependencies by lazy {
        classLogger.info("\t|=> Dependency Processor: Reading the 'outdated' map.")
        reportJson["outdated"] as Map<*, *>
    }
    val dependencies by lazy {
        classLogger.info("\t|=> Dependency Processor: Reading the 'outdated:dependencies' list")
        outdatedDependencies["dependencies"] as List<*>
    }

    fun isDependencyAnalysisValid() = jsonReportFile.exists() && dependencies.isNotEmpty()

    fun printDependenciesToUpgrade() = dependencies.forEach {
        val dependencyInformation = it as Map<*, *>
        val group = dependencyInformation["group"]
        val name = dependencyInformation["name"]
        val dependencyId = "$group:$name"
        val currentVersion = dependencyInformation["version"]
        val availableRelease = (it["available"] as Map<*, *>)["release"]
        val availableMilestone = (it["available"] as Map<*, *>)["milestone"]
        val availableIntegration = (it["available"] as Map<*, *>)["integration"]

        if (dependencyId !in restrictedDependencies) {
            classLogger.info(depLogLine, group, name, currentVersion, availableMilestone, availableIntegration, availableRelease ?: "N/A")
            println(depMsgLine.format(group, name, currentVersion, availableMilestone, availableIntegration, availableRelease ?: "N/A"))
        } else classLogger.debug(depAltLine, group, name, currentVersion, availableMilestone)
    }

    fun printDependencyUpdateReport() {
        when {
            !jsonReportFile.exists() -> {
                classLogger.error("ERROR: No dependency update report found.")
                println("::error file=build.gradle.kts::Dependency report not found at ${DependencyUpdatePolicy.FILE_PATH}")
                return
            }

            isDependencyAnalysisValid() -> printDependenciesToUpgrade().also { println(depMsgActive) }
            else -> classLogger.warn("All dependencies are up to date.").also {
                println("::notice file=build.gradle.kts::Dependencies are up to date.")
            }
        }
    }
}
