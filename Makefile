.PHONY: shellspec-bootstrap shellspec-run shellspec-clean

# Bootstrap ShellSpec locally into project
shellspec-bootstrap:
	bash src/test/sh/bootstrap-shellspec.sh

# Run tests via local ShellSpec install
shellspec-run:
	.local/bin/shellspec

# Clean local ShellSpec installation (force rebuild)
shellspec-clean:
	echo -e "A placeholder for now; until we know what do we want to clean up."
