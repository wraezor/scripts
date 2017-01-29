#!/bin/bash

MIRROR_ROOT=/data/Backup/Sites
CMD="wget"
CMD_OPTS="--mirror --no-parent --adjust-extension --restrict-file-names=windows --convert-links -p -w 10 -e robots=off"
DATESTAMP=$(date +"%Y%m%d")
CURRENT_DIR=$MIRROR_ROOT/$DATESTAMP

MIRROR_SITES=( \
	"www.truecovenanter.com" \
	"www.covenanter.org" \
	"www.apuritansmind.com" \
	"www.swrb.com" \
	"www.cmfnow.com" \
        "www.gracegems.org" \
        "www.reformedbooksonline.com" \
)

if [ -d "$CURRENT_DIR" ]; then
	rm -rf $CURRENT_DIR
fi

mkdir $CURRENT_DIR
cd $CURRENT_DIR

for SITE in "${MIRROR_SITES[@]}"
do
	echo "Mirroring $SITE..."
	$CMD $CMD_OPTS -P $CURRENT_DIR http://$SITE/
done

