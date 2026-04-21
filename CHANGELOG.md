# Changelog

## v2.1 (2026-04-18)

将共享质量框架快照内置到仓库中，安装后不再依赖外部 `prd-quality-framework` 目录。

### 可用性升级

- **框架快照随仓库分发**：新增 `references/framework/`，包含 `complexity-assessment.md`、`global-checks/` 与全部章节质量标准
- **本地路径替换外部硬编码**：`SKILL.md` 改为从 `references/framework/` 渐进加载，不再依赖外部共享 framework 目录
- **通用 Prompt 变为真正自包含**：`dist/create-prd-universal-prompt.md` 与 `dist/create-prd.skill` 重新内联框架文件，离线复制即可使用
- **安装流程简化**：新增根目录安装脚本，直接安装整个 skill 目录
- **完整工作流仓库**：README 增加 `PRD Productivity Toolkit` 独立仓库入口，便于获取 create/check/Feishu 协作的完整组合

## v2.0 (2026-04-17)

引入统一章节 × L 级复杂度质量框架（V2），与 `check-prd` 共享同一质量基线。

### 核心架构变化

- **引入共享 prd-quality-framework**：L1-L4 复杂度分级、G1/G2/G3 全局检查统一从 `references/framework/` 渐进加载
- **渐进加载强制要求**：阶段 0 加载 complexity-assessment + G1，阶段 1 每章先加载质量标准再加载生成指引，阶段 2 加载 G2+G3，其余时间不持有框架文件

### 阶段 0 升级

- L 级判定改用 `complexity-assessment.md §1` 四步法（用户感知描述 → 决策树 → 歧义消解 → 辅助信号）
- G1 产品类型判定：商业化 × 功能类型两轴，决定章节侧重和 dist 适用表
- 章节裁剪依据 `complexity-assessment.md §3` 章节适用表和 §4 产品类型叠加规则

### 阶段 1 升级

- 每章生成前先加载 `prd-quality-framework/chapters/chN-*.md`（质量标准/写作目标）
- 再加载 `references/chapters/create-prd-chN-*.md`（模板/Mermaid/表格结构）
- 写完立即输出，释放两个文件上下文，进入下一章
- L 级 Must 项必须命中，Should 项择优覆盖

### 阶段 2 自检（L3/L4 必做）

- G2 文档结构完整性：Ch1→Ch4→Ch10 逻辑链路（最核心）、Ch10 三块对齐、Ch4→Ch11 可度量性、Ch6→Ch12 自洽
- G3 重大风险 R1-R8：扫描高严重度风险并写入文末"附：待完善清单"

### dist 说明

- `dist/create-prd-universal-prompt.md` 包含 SKILL.md + 所有 references/chapters/ 内容
- 注意：自 v2.1 起，质量标准文件（`references/framework/`）已经重新内联到 dist，universal prompt 无需额外依赖即可单独使用

## v1.0 (2026-04-02)

- 初始版本
- 14 章结构化 PRD 生成，支持逐章即时输出
- 产品定型机制（商业化产品 vs 企业自研系统 × 四种功能类型）
- 基于《决胜B端》《决胜体验设计》《决胜B端PRD模板v2.0》构建
- 生成后自动执行轻量自检，输出待完善清单
- 支持 Claude Code skill 集成和任意大模型通用 prompt
