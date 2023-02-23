test:
	@bash -c "\
		cd rfast; \
		maturin develop --release -- -C target-cpu=native; \
		EXIT_CODE=$?; \
		cd ..; \
		echo \"code ${EXIT_CODE}\"; \
		if [ -z \"${EXIT_CODE}\" ]; then \
			pytest tests/test.py; \
		else \
			echo \"compile failed\"; \
		fi \
	"
