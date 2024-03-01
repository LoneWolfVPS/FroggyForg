import sys

# this will break any attempt to import xformers which will prevent stability diffusion repo from trying to use it
if "--xformers" not in "".join(sys.argv):
    sys.modules["xformers"] = None

# Hack to fix a changed import in torchvision 0.17+, which otherwise breaks
# basicsr; see https://github.com/A U T O M A T I C 1 1 1 1 / s t a b l e - d i f f u s i o n - w e b u i/issues/13985
try:
    import torchvision.transforms.functional_tensor  # noqa: F401
except ImportError:
    try:
        import torchvision.transforms.functional as functional
        sys.modules["torchvision.transforms.functional_tensor"] = functional
    except ImportError:
        pass  # shrug...
