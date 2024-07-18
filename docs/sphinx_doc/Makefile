# Makefile

SPHINXBUILD   = sphinx-build
SPHINXPROJ    = App-Controller-Doc
ASSETSDIR     = assets
BUILDDIR      = build/html
SOURCEDIR_EN  = en/source
BUILDDIR_EN   = build/html/en
SOURCEDIR_ZH  = zh_CN/source
BUILDDIR_ZH   = build/html/zh_CN

# English document
en:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR_EN)" "$(BUILDDIR_EN)"
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR_EN)"

index:
	@cp "$(ASSETSDIR)/redirect.html" "$(BUILDDIR)/index.html"

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR_EN)" "$(BUILDDIR_EN)" $(O)

all: en index

.PHONY: all en index