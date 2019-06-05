dist_folder = nickglenn_dev_tools

release:
ifndef version
	$(error You must specify a release version with hyphens in place of dots: 2019-x)
endif
	mkdir -p builds
	rm -rf builds/${dist_folder}
	rsync -r \
		--exclude='*/__pycache__' \
		plugin/ builds/${dist_folder}
	rm -rf builds/dev_tools-${version}.zip
	cd builds && zip -r dev_tools-${version}.zip ${dist_folder}
	echo "Bundle is ready:  builds/dev_tools-${version}.zip"