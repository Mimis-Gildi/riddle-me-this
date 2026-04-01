import org.asciidoctor.gradle.jvm.AsciidoctorTask
import org.asciidoctor.gradle.jvm.epub.AsciidoctorEpubTask
import org.asciidoctor.gradle.jvm.epub.AsciidoctorEpubTask.EPUB3
import org.asciidoctor.gradle.jvm.pdf.AsciidoctorPdfTask
import org.slf4j.LoggerFactory

val useJavaVersion: String by project
val resumeFolder = file(project.property("resume.root.folder") as String)

val resumeDate: String by project
val resumeVersion: String by project


val pdfResumeThemeIds = listOf(
    "conservative-resume",
    "creative-resume",
    "engineering-resume",
    "core-resume"
    )

private val log by lazy { LoggerFactory.getLogger("me.riddle.the.build") }

plugins {
    `kotlin-dsl`
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
        vendor.set(JvmVendorSpec.ADOPTIUM)
        log.info("\t|=> Riddle me that Java Toolchain SET to    -> $useJavaVersion : ${JvmVendorSpec.ADOPTIUM}.")
    }
}

dependencies {
    api(libs.slf4j.api)
    implementation(libs.kotlin.logging)
    implementation(libs.logback.classic)
}

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
            themeDir = file(resumeFolder)
            themeName = themeId
        }
    }
}

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
        "VadimKuhay-Resume.adoc")
) {
    task.apply {
        isLogDocuments = true
        baseDirFollowsSourceDir()
        sourceDir(sourceDir)

        sources { includePatterns.forEach { include(it) } }

        attributes(
            mapOf(
                "revision-date" to resumeDate,
                "revision-number" to resumeVersion
            )
        )
    }
}
