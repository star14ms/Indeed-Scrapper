from scrapper.so import extract_stack_pages, extract_stack_jobs
# from scrapper.save import save_to_file

last_stack_pages = extract_stack_pages()
stack_jobs = extract_stack_jobs(last_stack_pages)
# save_to_file(stack_jobs)