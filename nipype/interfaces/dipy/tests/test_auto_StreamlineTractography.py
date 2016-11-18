# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..tracks import StreamlineTractography


def test_StreamlineTractography_inputs():
    input_map = dict(gfa_thresh=dict(mandatory=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(mandatory=True,
    ),
    in_model=dict(),
    in_peaks=dict(),
    min_angle=dict(mandatory=True,
    usedefault=True,
    ),
    multiprocess=dict(mandatory=True,
    usedefault=True,
    ),
    num_seeds=dict(mandatory=True,
    usedefault=True,
    ),
    out_prefix=dict(),
    peak_threshold=dict(mandatory=True,
    usedefault=True,
    ),
    save_seeds=dict(mandatory=True,
    usedefault=True,
    ),
    seed_coord=dict(),
    seed_mask=dict(),
    tracking_mask=dict(),
    )
    inputs = StreamlineTractography.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_StreamlineTractography_outputs():
    output_map = dict(gfa=dict(),
    odf_peaks=dict(),
    out_seeds=dict(),
    tracks=dict(),
    )
    outputs = StreamlineTractography.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
