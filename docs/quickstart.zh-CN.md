# 快速开始

## 环境

- Python 3.11+
- `pip install -r requirements.txt`
- GNU Make
- Git

## 1. 检查仓库

```bash
make check
```

会运行公共仓库卫生检查，并编译所有 Python 文件。

## 2. 跑测试

```bash
pip install pytest
make test
```

测试覆盖卫生规则、card hash 行为和端到端 demo。

## 3. 跑最小事务

```bash
make demo
```

demo 会在 `examples/minimal-run/_run` 下创建临时 run，渲染一张任务卡，写入一份 submission 和一个 artifact，然后跑四个 gate：

```text
g0_schema -> g1_scope -> g2_evidence -> g3_command
```

预期结果：

```json
{"ok": true, "task_id": "T-001", "attempt": 1, "verdict": "PASS"}
```

demo 结束后会自动清理临时 run 和 artifact。

## 4. 继续阅读

- [概念](concepts.md)
- [协议](protocol.md)
- [架构](architecture.md)
- [可复现性](reproducibility.md)
- [限制](limitations.md)
- [安全模型](security-model.md)

## demo 证明什么

它证明事务机制可以工作：

```text
card -> 单 seat -> submission -> gates -> ledger
```

它**不**证明内容语义正确。语义正确由独立 Review 负责，不由 Gate 负责。
