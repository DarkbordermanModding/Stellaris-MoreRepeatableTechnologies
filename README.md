# Stellaris-MoreRepeatableTechnologies


## Prerequisite

* gettext-base 0.19.8.1
* make 4.2.1
* steamcmd:i386 0~20180105-3
* github-cli 2.10.1
* jq 1.6

## Uploading to workshop

1. Create environment variables
```
cp sample.env .env
```

2. Publish to Steam workshop
```
make upload_workshop
```

3. (Optional) Update Github repository information
```
make update_github_info
```
