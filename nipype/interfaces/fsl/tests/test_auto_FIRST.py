# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import FIRST


def test_FIRST_inputs():
    input_map = dict(affine_file=dict(argstr='-a %s',
    position=6,
    ),
    args=dict(argstr='%s',
    ),
    brain_extracted=dict(argstr='-b',
    position=2,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-i %s',
    copyfile=False,
    mandatory=True,
    position=-2,
    ),
    list_of_specific_structures=dict(argstr='-s %s',
    position=5,
    sep=',',
    ),
    method=dict(argstr='-m %s',
    position=4,
    usedefault=True,
    xor=[u'method_as_numerical_threshold'],
    ),
    method_as_numerical_threshold=dict(argstr='-m %.4f',
    position=4,
    ),
    no_cleanup=dict(argstr='-d',
    position=3,
    ),
    out_file=dict(argstr='-o %s',
    hash_files=False,
    mandatory=True,
    position=-1,
    usedefault=True,
    ),
    output_type=dict(),
    terminal_output=dict(nohash=True,
    ),
    verbose=dict(argstr='-v',
    position=1,
    ),
    )
    inputs = FIRST.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_FIRST_outputs():
    output_map = dict(bvars=dict(),
    original_segmentations=dict(),
    segmentation_file=dict(),
    vtk_surfaces=dict(),
    )
    outputs = FIRST.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
