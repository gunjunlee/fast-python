test:
	@bash -c "\
		cd rfast; \
		maturin develop --rustc-extra-args=\"-C target-cpu=native\" --release; \
		EXIT_CODE=$?; \
		cd ..; \
		echo \"code ${EXIT_CODE}\"; \
		if [ -z \"${EXIT_CODE}\" ]; then \
			pytest tests/test.py; \
		else \
			echo \"compile failed\"; \
		fi \
	"
