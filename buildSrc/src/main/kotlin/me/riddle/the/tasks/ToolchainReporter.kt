package me.riddle.the.tasks

import org.gradle.api.Project
import org.gradle.api.logging.Logger
import org.gradle.jvm.toolchain.JavaLanguageVersion
import org.gradle.jvm.toolchain.JavaToolchainService

/**
 * Provides diagnostic reporting for a configured Java toolchain.
 *
 * This class allows structured inspection and dual-mode reporting (IDE logging + GitHub Actions annotations)
 * for the Java launcher resolved by Gradle’s Toolchain API.
 *
 * It is intended to be used from custom Gradle tasks such as `verifyJavaToolchain`.
 *
 * @param project the Gradle [Project] context in which this reporter is used.
 * @param logger the Gradle [Logger] used for structured output in local builds.
 */
class ToolchainReporter(
    private val project: Project,
    private val logger: Logger
) {
    /**
     * Resolves the specified Java toolchain version and logs detailed metadata
     * to both the Gradle logger and GitHub Actions-compatible annotations.
     *
     * This method is typically invoked within a `doLast` block of a custom task.
     *
     * @param javaVersion the Java language version to resolve using the Toolchain API.
     */
    fun reportJavaToolchain(javaVersion: Int) {
        val launcher = project.extensions
            .getByType(JavaToolchainService::class.java)
            .launcherFor {
                languageVersion.set(JavaLanguageVersion.of(javaVersion))
            }.get()

        val metadata = launcher.metadata

        logger.info("\t|=> Riddle me that Java Toolchain        -> ${metadata.installationPath}")
        printlnNotice("Vendor", metadata.vendor)
        printlnNotice("Language Version", metadata.languageVersion.toString())
        printlnNotice("JVM Version", metadata.jvmVersion)
        printlnNotice("Java Runtime Version", metadata.javaRuntimeVersion)
        @Suppress("UnstableApiUsage")
        (printlnNotice("Is Current JVM?", metadata.isCurrentJvm.toString()))
    }

    /**
     * Emits a GitHub Actions-compatible `::notice` message for visibility in CI logs.
     *
     * @param label the label of the diagnostic field (e.g., "Vendor").
     * @param value the value to be displayed alongside the label.
     */
    private fun printlnNotice(label: String, value: String) {
        println("::notice file=build.gradle.kts task=verifyJavaToolchain::$label -> $value")
    }
}
