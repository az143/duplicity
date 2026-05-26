
## Release Duplicity

1. merge dev into main
2. get Crowdin updates
    - run "make pot"
    - commit "chg:pkg: Run po/update-pot."
    - wait for Crowdin MR
    - fix & merge Crowdin MR
      - add chg:pkg: to title
      - click 'squash commits' and 'delete branch'
3. run "tools/release-prep \<version\>"
4. push to origin/main
5. Launchpad PPAs
    - [Develop PPA](https://code.launchpad.net/~duplicity-team/+recipe/duplicity-develop-git)
    - [Release PPA](https://code.launchpad.net/~duplicity-team/+recipe/duplicity-release-git)
    - edit the "Recipe contents" at the bottom to update the version number
6. Launchpad SNAPs
    - [Develop SNAP](https://launchpad.net/~duplicity-team/duplicity/+snap/duplicity-dev)
    - [Release SNAP](https://launchpad.net/~duplicity-team/duplicity/+snap/duplicity-rel)
    - double check the settings so nothing is automatic
7. run "git push alpha : --tags"
8. run "git push mirror : --tags"
9. "request builds" on both PPAs and SNAPS
10. release pip version
    - if the last pipeline for `main` was skipped:
      - set CI_COMMIT_MESSAGE to "push"
      - run new pipeline for `main`
    - run job `wheels` once done
11. update web pages in duplicity.gitlab.io
    - set new version and date in index.wml
    - commit and push
12. release to GitLab releases
13. send email to talk and announce
14. send backup tarballs to sourceforge.net
15. merge main into dev
16. set next version in dev, e.g. 3.0.1-->3.0.2.dev0
17. check builds for Launchpad PPAs and SNAPs

## Versioning

 - We use [semantic versioning](https://semver.org/).
 - Dev releases are numbered like `3.0.3.dev0`.
 - Full releases are numbered like `3.0.2`.
 - We use `git tag rel.3.0.3.dev0` to mark dev releases.
 - We use `git tag rel.3.0.2` to mark full releases.
 - We no longer use alpha, beta, or rc for releases.
