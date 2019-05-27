make:
	(cd src ; $(MAKE) )
	(cd tools ; $(MAKE) )
	(cd lio ; make again )
clean: 
	@echo "==> Cleaning object, library, and executable files"
	-rm -r bin 
	(cd src ; $(MAKE) clean)
