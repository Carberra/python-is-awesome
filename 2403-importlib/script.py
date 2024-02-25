# from pkg_resources import get_distribution

# dist = get_distribution("analytix")
# print(dist.version)

from importlib import metadata, resources

print(metadata.version("analytix"))
print(metadata.entry_points(name="black"))
print(metadata.files("analytix"))

print(list(resources.files("analytix").glob("*.py")))
print(resources.open_text("analytix", "client.py").read())
