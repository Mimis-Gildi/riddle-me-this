@file:Suppress("unused")

package me.riddle.the.dependencies

/**
 * Root dependency model by Ben Manes.
 *
 * Placeholder for Captain's refactoring.
 */
data class BenManesDependencyEntry(
    val group: String,
    val name: String,
    val version: String,
    val projectUrl: String?,
    val userReason: String?,
    val available: AvailableVersions
)

data class AvailableVersions(val release: String, val milestone: String, val integration: String)

