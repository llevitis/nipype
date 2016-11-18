# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..specialized import BRAINSTransformFromFiducials


def test_BRAINSTransformFromFiducials_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fixedLandmarks=dict(argstr='--fixedLandmarks %s...',
    ),
    fixedLandmarksFile=dict(argstr='--fixedLandmarksFile %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    movingLandmarks=dict(argstr='--movingLandmarks %s...',
    ),
    movingLandmarksFile=dict(argstr='--movingLandmarksFile %s',
    ),
    numberOfThreads=dict(argstr='--numberOfThreads %d',
    ),
    saveTransform=dict(argstr='--saveTransform %s',
    hash_files=False,
    ),
    terminal_output=dict(nohash=True,
    ),
    transformType=dict(argstr='--transformType %s',
    ),
    )
    inputs = BRAINSTransformFromFiducials.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_BRAINSTransformFromFiducials_outputs():
    output_map = dict(saveTransform=dict(),
    )
    outputs = BRAINSTransformFromFiducials.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
