update_github_info:
	gh repo edit --add-topic `jq -r '.topics | join(",")' gh_config.json`
	gh repo edit --homepage `jq -r '.homepage' gh_config.json`
	gh repo edit --description "`jq -r '.description' gh_config.json`"
	gh repo edit --enable-wiki=`jq -r '.enable_wiki' gh_config.json`
