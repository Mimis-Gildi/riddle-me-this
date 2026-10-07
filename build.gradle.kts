import org.asciidoctor.gradle.jvm.AbstractAsciidoctorTask
import org.asciidoctor.gradle.jvm.AsciidoctorTask
import org.asciidoctor.gradle.jvm.epub.AsciidoctorEpubTask
import org.asciidoctor.gradle.jvm.epub.AsciidoctorEpubTask.EPUB3
import org.asciidoctor.gradle.jvm.pdf.AsciidoctorPdfTask

// @formatter:off
private val resumeFolderName    by lazy { providers.gradleProperty("resume.root.folder").get() }
private val themesFolderName    by lazy { "$resumeFolderName/themes" }
private val resumeDate          by lazy { providers.gradleProperty("resumeDate").get() }
private val resumeVersion       by lazy { providers.gradleProperty("resumeVersion").get() }
private val resumeFolder        by lazy { file(resumeFolderName) }
private val themesFolder        by lazy { file(themesFolderName) }
// @formatter:on

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

kotlin {
    jvmToolchain {
        languageVersion.set(JavaLanguageVersion.of(libs.versions.java.get()))
        vendor.set(JvmVendorSpec.ADOPTIUM)
        logger.lifecycle("\t|=> Riddle me that Java Toolchain SET to    -> ${libs.versions.java.get()} : ${JvmVendorSpec.ADOPTIUM}.")

    }
}

dependencies {
    api(libs.slf4j.api)
    implementation(libs.kotlin.logging)
    implementation(libs.logback.classic)
}

tasks.named<Jar>("jar") {
    logger.lifecycle("\t|=> Riddle me that Jar Task is used as a dependency here, and thus explicitly disabled!")
    enabled = false
}

tasks.named<AsciidoctorTask>("asciidoctor") { configureAsciiDocInput(this) }

tasks.named<AsciidoctorPdfTask>("asciidoctorPdf") { configureAsciiDocInput(this) }

tasks.named<AsciidoctorEpubTask>("asciidoctorEpub") { configureAsciiDocInput(this).also { ebookFormats(EPUB3) } }

/**
 * Configures the Asciidoctor task to generate documents from a specified source directory
 * and include only the specified patterns.
 *
 * @param task the Asciidoctor task to configure
 * @param sourceDir the source directory containing the documents to generate
 * @param includePatterns the patterns to include in the generation. Defaults to ["VadimKuhay-Resume.adoc"]
 */
fun configureAsciiDocInput(
    task: AbstractAsciidoctorTask,
    sourceDir: File = resumeFolder,
    includePatterns: List<String> = listOf(
        "VadimKuhay-Resume.adoc"
    )
) {
    task.apply {
        isLogDocuments = true
        baseDirFollowsSourceDir()
        sourceDir(sourceDir)

        sources { includePatterns.forEach { include(it) } }

        attributes(
            mapOf(
                "revision-date" to resumeDate,
                "revision-number" to resumeVersion,
                "pdf-themesdir" to themesFolder.absolutePath
            )
        )
    }
}
