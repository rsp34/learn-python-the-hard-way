# Create a template for the different strings
formatter = "%r %r %r %r"

# Print different strings using the template
print formatter % (1, 2, 3, 5)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing",
	"That you could type up right",
	"But it didn't sing.",
	"So I said goodnight"
)