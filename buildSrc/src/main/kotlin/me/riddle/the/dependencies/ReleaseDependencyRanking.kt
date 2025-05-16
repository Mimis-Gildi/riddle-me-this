package me.riddle.the.dependencies

import me.riddle.the.dependencies.GitHubActionsAnnotations.RELEASE_ONLY_BY_ENV_VAR
import me.riddle.the.dependencies.GitHubActionsAnnotations.RELEASE_ONLY_BY_PROPERTY
import me.riddle.the.dependencies.GitHubActionsAnnotations.RELEASE_ONLY_DISABLED
import me.riddle.the.dependencies.ReleaseDependencyRanking.RELEASE_RESTRICTION_ENVIRONMENT_VARIABLE
import me.riddle.the.dependencies.ReleaseDependencyRanking.RELEASE_RESTRICTION_PROPERTY_NAME
import org.gradle.api.Project
import org.slf4j.Logger
import org.slf4j.LoggerFactory

private val localLogger by lazy { LoggerFactory.getLogger("me.riddle.the.dependencies") }

object  ReleaseDependencyRanking {
    const val RELEASE_RESTRICTION_ENVIRONMENT_VARIABLE = "RELEASES_ONLY"
    const val RELEASE_RESTRICTION_PROPERTY_NAME = "useReleaseDependenciesOnly"
}
object GitHubActionsAnnotations {

    const val RELEASE_ONLY_BY_PROPERTY = "::notice file=build.gradle.kts::Release-only dependencies enforced by project property. (by {})"
    const val RELEASE_ONLY_BY_ENV_VAR = "::notice file=build.gradle.kts::Release-only dependencies enforced by environment variable. (by {})"
    const val RELEASE_ONLY_DISABLED = "::notice file=build.gradle.kts::Release-only restriction disabled. Enable by setting property $RELEASE_RESTRICTION_PROPERTY_NAME or by setting environment variable $RELEASE_RESTRICTION_ENVIRONMENT_VARIABLE."
}

object DependencyUpdatePolicy {
    const val PROCESS_NAME = "processDependencyUpdates"
    const val TASK_NAME = "dependencyUpdates"
    const val CHECK_GRADLE = true
    const val FORMAT = "json"
    const val FOLDER = "build/dependencies"
    const val FILE_NAME = "dependency-update-report"
    val FILE_PATH get() = "$FOLDER/$FILE_NAME.$FORMAT"
}

/**
 * Checks if the project should use release-only dependencies or not.
 *
 * This method first checks the project property [RELEASE_RESTRICTION_PROPERTY_NAME] and if it is set to true.
 * If not, it checks the environment variable [RELEASE_RESTRICTION_ENVIRONMENT_VARIABLE] and if it is set to true.
 * If neither of them are set to true, it means that the project should not use release-only dependencies.
 *
 * @return true if the project should use release-only dependencies, false otherwise.
 */
fun Project.shouldUseReleaseOnlyDependencies(log: Logger = localLogger): Boolean {
    val prop = findProperty(RELEASE_RESTRICTION_PROPERTY_NAME)?.toString()?.toBoolean() ?: false
    val env = System.getenv(RELEASE_RESTRICTION_ENVIRONMENT_VARIABLE)?.toBoolean() ?: false

    when {
        prop -> log.info(RELEASE_ONLY_BY_PROPERTY,log.name)
        env -> log.info(RELEASE_ONLY_BY_ENV_VAR, log.name)
        else -> log.warn(RELEASE_ONLY_DISABLED)
    }

    return prop || env
}
