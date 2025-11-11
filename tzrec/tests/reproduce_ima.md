# Steps

## 1. env

machine:
> A10

docker image:
> mybigpai-public-registry.cn-beijing.cr.aliyuncs.com/easyrec/tzrec-devel:0.9-cu126

## 2. dependency

```shell
# 1. clone latest recsys-examples

# 2.
pip install ninja

# 3. install latest dynamicemb

# 4.
git clone https://github.com/jiashuy/TorchEasyRec.git
cd TorchEasyRec
bash scripts/gen_proto.sh
pip install -r requirements.txt
PYTHONPATH=. python tzrec/tests/rank_integration_test.py RankIntegrationTest.test_multi_tower_din_with_dynamicemb_train_eval

# 5 error and output log in under 
tmp/tzrec_v7qw3x15/log_train_eval/1107b01e-2e3c-44ed-b5f9-c055328a5375_oj8niyta/attempt_0/0/stdout.log
```