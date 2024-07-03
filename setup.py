from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

SOURCE_DIR = "src/syndiff/utils/op"

setup(
    ext_modules=[
        CUDAExtension(
            name="upfirdn2d_op",
            sources=[
                f"{SOURCE_DIR}/upfirdn2d.cpp",
                f"{SOURCE_DIR}/upfirdn2d_kernel.cu",
            ],
            extra_compile_args={"cxx": ["-g"], "nvcc": ["-O2"]},
            extra_link_flags=["-Wl,--no-as-needed", "-lcuda"],
        ),
        CUDAExtension(
            name="fused",
            sources=[
                f"{SOURCE_DIR}/fused_bias_act.cpp",
                f"{SOURCE_DIR}/fused_bias_act_kernel.cu",
            ],
            extra_compile_args={"cxx": ["-g"], "nvcc": ["-O2"]},
            extra_link_flags=["-Wl,--no-as-needed", "-lcuda"],
        )
    ],
    cmdclass={"build_ext": BuildExtension},
)
