# src/test/sh/export-issues-for-saga_spec.sh

Describe 'export-issues-for-saga.sh'

  BeforeEach 'setup'
  AfterEach 'cleanup'

  setup() {
    mkdir -p .saga-notes/letters
    touch .saga-notes/letters/index.text
  }

  cleanup() {
    rm -rf .saga-notes
  }

  It 'exports known real issues from live repository'
    When run script src/main/sh/export-issues-for-saga.sh 11 16 18
    The output should include "Exporting issue #11."
    The output should include "Exporting issue #16."
    The output should include "Exporting issue #18."
    The output should include "✅ Export complete"
    The file ".saga-notes/letters/issues-for-saga.json" should be exist
  End
End
