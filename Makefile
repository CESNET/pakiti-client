all: man

install: install-client

install-client:
	install -D pakiti-client $(DESTDIR)/usr/bin/pakiti-client

man:
	pod2man -c "System Manager's Manual" -r 'pakiti v3' pakiti-client > pakiti-client.1

clean:
	$(RM) pakiti-client.1

.PHONY: all install install-client man
