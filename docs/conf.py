project = "greet-docs"
extensions = ["sphinx.ext.apidoc"]
apidoc_modules = [
    {
        "path": "../src/greet_docs",
        "destination": "reference",
    }
]
