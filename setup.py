import cx_Freeze

executables = [cx_Freeze.Executable(
    script="jogodobatman.py",
    icon="jogodobatman/baticon.png"
)]
cx_Freeze.setup(
    name="Batman Vs Croc",
    options={
        "build_exe":{"packages":["pygame"],
        "include_files":["jogodobatman"]
        }}
    ,executables = executables
)