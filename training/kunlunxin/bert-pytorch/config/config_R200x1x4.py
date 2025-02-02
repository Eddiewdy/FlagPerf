from config_common import *

fp16 = False
ddp_type = "apex"
#dist_backend = "nccl"
dist_backend = "xccl"
use_xpu = True
use_env = True
gradient_accumulation_steps = 1
train_batch_size = 12
max_steps = 1000000
start_warmup_step = 0
warmup_proportion = 0
warmup_steps = 1000

distributed_lamb = False
learning_rate = 1.4e-4
weight_decay_rate = 0.01
opt_lamb_beta_1 = 0.9
opt_lamb_beta_2 = 0.999

eval_batch_size = train_batch_size
max_samples_termination = 45000000
cache_eval_data = True

fused_gelu_bias = False
fused_mha = False
dense_seq_output = False
exchange_padding = False

dwu_num_rs_pg = 1
dwu_num_ar_pg = 1
dwu_num_blocks = 1

seed = 9031
