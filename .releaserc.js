module.exports = {
    "branches": '"${result}"',
    "plugins": [
      [
        "@semantic-release/commit-analyzer",
        {
          "preset": "conventionalcommits"
        }
      ],
      [
        "@semantic-release/release-notes-generator",
        {
          "preset": "conventionalcommits"
        }
      ],
      "@semantic-release/changelog",
      "@semantic-release/gitlab",
      "@semantic-release/git"
    ]
}
