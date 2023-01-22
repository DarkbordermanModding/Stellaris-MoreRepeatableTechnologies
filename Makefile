include .env
export

generate_vdf:
	envsubst < template.vdf > workshop.vdf

upload_workshop: generate_vdf
	steamcmd +login ${AUTHOR} +workshop_build_item ${PWD}/workshop.vdf +quit

update_github_info:
	gh repo edit --add-topic `jq -r '.topics | join(",")' gh_config.json`
	gh repo edit --homepage `jq -r '.homepage' gh_config.json`
