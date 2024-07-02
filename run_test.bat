

set CWD=%cd%
set PATH=%PATH%;D:\lloyd\dev\software\ninja-win
call "C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Auxiliary\Build\vcvars64.bat"


python test.py ^
    --image_size 256 ^
    --exp Brats_T1_T2 ^
    --num_channels 2 --num_channels_dae 64 --ch_mult 1 1 2 2 4 4 --num_timesteps 4 --num_res_blocks 2 --batch_size 1 --embedding_type positional  --z_emb_dim 256 ^
    --which_epoch 50 ^
    --gpu_chose 0 ^
    --contrast1 T1  --contrast2 T2 ^
    --input_path %CWD%\SynDiff_sample_data ^
    --output_path %CWD%\checkpoints
