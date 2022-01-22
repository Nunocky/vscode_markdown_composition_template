all:
	@/usr/bin/env python3 ./bin/concat.py

clean:
	$(RM) -f *~ INPUT.md

.PHONY: all clean
