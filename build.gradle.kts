import com.github.benmanes.gradle.versions.updates.DependencyUpdatesTask
import me.riddle.the.dependencies.*
import me.riddle.the.tasks.registerVerifyToolchainTask
import org.asciidoctor.gradle.jvm.AsciidoctorTask
import org.asciidoctor.gradle.jvm.epub.AsciidoctorEpubTask
import org.asciidoctor.gradle.jvm.epub.AsciidoctorEpubTask.EPUB3
import org.asciidoctor.gradle.jvm.pdf.AsciidoctorPdfTask
import org.slf4j.LoggerFactory
import java.util.*

val useJavaVersion: String by project
val resumeFolder = file(project.property("resume.root.folder") as String)

val pdfResumeThemeIds = listOf(
    "conservative-resume",
    "creative-resume",
    "technical-resume",
    )

private val log by lazy { LoggerFactory.getLogger("me.riddle.the.build") }

plugins {
    `kotlin-dsl`

    alias(libs.plugins.ben.manes)
    alias(libs.plugins.dokka)

    alias(libs.plugins.asciidoctor.jvm.pdf)
    alias(libs.plugins.asciidoctor.jvm.gems)
    alias(libs.plugins.asciidoctor.jvm.epub)
    alias(libs.plugins.asciidoctor.jvm.convert)
}

allprojects {
    repositories {
        mavenCentral()
    }
}

java {
    toolchain {
        languageVersion.set(JavaLanguageVersion.of(useJavaVersion))
        vendor.set(JvmVendorSpec.ADOPTIUM) // Temurin
        log.info("\t|=> Riddle me that Java Toolchain SET to    -> $useJavaVersion : ${JvmVendorSpec.ADOPTIUM}.")
    }
}

dependencies {
    implementation(gradleApi())
    implementation(platform(kotlin("bom")))

    api(libs.slf4j.api)
    implementation(libs.kotlin.logging)
    implementation(libs.logback.classic)
}

registerVerifyToolchainTask()


tasks.named<Jar>("jar") {
    log.info("\t|=> Riddle me that Jar Task is used as a dependency here, and thus explicitly disabled!")
    enabled = false
}

tasks.named<AsciidoctorTask>("asciidoctor") { configureAsciiDocInput(this) }

tasks.named<AsciidoctorPdfTask>("asciidoctorPdf") { configureAsciiDocInput(this) }

tasks.named<AsciidoctorEpubTask>("asciidoctorEpub") { configureAsciiDocInput(this).also { ebookFormats(EPUB3) } }

pdfThemes {
    pdfResumeThemeIds.forEach { themeId ->
        local(themeId) {
            themeDir = file("resources/themes")
            themeName = themeId
        }
    }
}

/**
 * Configures the dependency update task to be run on build at will.
 */
tasks.named<DependencyUpdatesTask>(DependencyUpdatePolicy.TASK_NAME).configure {
    checkForGradleUpdate = DependencyUpdatePolicy.CHECK_GRADLE
    outputFormatter = DependencyUpdatePolicy.FORMAT
    outputDir = DependencyUpdatePolicy.FOLDER
    reportfileName = DependencyUpdatePolicy.FILE_NAME

    rejectVersionIf { shouldUseReleaseOnlyDependencies(log) && isStableVersion(candidate.version).not() }
}

/**
 * Triggers Ben's dependency update process and extracts suggestions for outdated dependencies.
 */
tasks.register(DependencyUpdatePolicy.PROCESS_NAME) {
    dependsOn(DependencyUpdatePolicy.TASK_NAME)

    doLast { LegacyOutdatedDependenciesProcessor(file(DependencyUpdatePolicy.FILE_PATH), log).printDependencyUpdateReport() }
}

tasks.named(DependencyUpdatePolicy.PROCESS_NAME) { outputs.upToDateWhen { false } }


/**
 * Configures the Asciidoctor task to generate documents from a specified source directory
 * and include only the specified patterns.
 *
 * @param task the Asciidoctor task to configure
 * @param sourceDir the source directory containing the documents to generate
 * @param includePatterns the patterns to include in the generation. Defaults to ["OnLeadership.adoc"]
 */
fun configureAsciiDocInput(
    task: org.asciidoctor.gradle.jvm.AbstractAsciidoctorTask,
    sourceDir: File = resumeFolder,
    includePatterns: List<String> = listOf(
        "OnLeadership.adoc",
        "OnEngineering.adoc")
) {
    task.apply {
        isLogDocuments = true
        baseDirFollowsSourceDir()
        sourceDir(sourceDir)

        sources { includePatterns.forEach { include(it) } }
    }
}

/**
 * Returns true if the given version string is considered stable.
 *
 * A stable version is one that contains the string "RELEASE", "FINAL", or "GA" (case-insensitive), or matches the
 * regular expression "^[0-9,.v-]+(-r)?$". The regular expression allows for versions with numbers, commas,
 * periods, "v" characters, hyphens, and optional "-r" suffixes.
 *
 * @param version the version string to check
 * @return true if the version is stable, false otherwise
 */
fun isStableVersion(version: String): Boolean {
    val stableKeyword = listOf("RELEASE", "FINAL", "GA").any { version.uppercase(Locale.getDefault()).contains(it) }
    val regex = "^[0-9,.v-]+(-r)?$".toRegex()
    val isStable = stableKeyword || regex.matches(version)
    return isStable
}