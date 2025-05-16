plugins {
    `kotlin-dsl`
    alias(libs.plugins.dokka)
}

repositories {
    mavenCentral()
    gradlePluginPortal()
}

dependencies {
    compileOnly(gradleApi())
    implementation(platform(kotlin("bom")))

    api(libs.slf4j.api)
    implementation(libs.kotlin.logging)
    implementation(libs.logback.classic)
}