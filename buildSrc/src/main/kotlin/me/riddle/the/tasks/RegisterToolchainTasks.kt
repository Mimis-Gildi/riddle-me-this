package me.riddle.the.tasks

import org.gradle.api.Project

/**
 * Registers a `verifyJavaToolchain` task for the calling [Project].
 *
 * This task logs detailed toolchain information — including Java vendor, language version,
 * and runtime metadata — using both the Gradle logger and GitHub Actions annotations.
 *
 * The resolved Java version is read from the `useJavaVersion` project property,
 * falling back to version `21` if unspecified.
 *
 * Usage in your `build.gradle.kts`:
 * ```
 * import me.riddle.the.tasks.registerVerifyToolchainTask
 *
 * registerVerifyToolchainTask()
 * ```
 */
fun Project.registerVerifyToolchainTask() {
    val log = logger
    val version = findProperty("useJavaVersion")?.toString()?.toIntOrNull() ?: 21

    tasks.register("verifyJavaToolchain") {
        group = "verification"
        description = "Prints information about the resolved Java Toolchain for debugging"

        doLast {
            ToolchainReporter(this@registerVerifyToolchainTask, log).reportJavaToolchain(version)
        }
    }
}
