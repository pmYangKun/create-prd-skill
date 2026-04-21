---
name: create-prd
description: 根据用户提供的业务上下文，生成结构化的 B端 PRD 文档（含初始内容）。当用户要求创建、撰写、生成 PRD、需求文档、产品方案、系统设计文档时自动触发，即使用户只说"帮我写个 PRD/方案/需求文档"。
---

# create-prd

根据用户提供的业务上下文和需求背景，生成结构化的、带有初始内容的 B端 PRD 文档。

支持显式调用（如 `/create-prd`）和自动触发（当用户明确要求创建、撰写 PRD、需求文档、产品方案或企业系统设计时）。

## 输入

- 用户提供的业务上下文和需求背景（自由文本、会议纪要、简要描述等均可）
- 或通过 `$ARGUMENTS` 传入的文件路径

如有参数传入，优先作为输入源：

$ARGUMENTS

---

## 质量基线：prd-quality-framework

本 skill 与 `check-prd` 共享一套质量基线——`references/framework/`。

- **complexity-assessment.md**：L1-L4 判定 + 章节适用表 + 产品类型叠加
- **global-checks/g1-product-type-fit.md**：产品类型契合度
- **global-checks/g2-document-structure.md**：文档结构完整性（自检）
- **global-checks/g3-major-risks.md**：重大风险 R1-R8（自检）
- **chapters/chN-*.md**：每个章节的 L1-L4 质量标准（写作目标）

**加载原则：渐进式**——只在当前阶段加载必要文件，不要预读整个框架。

---

## 生成流程

严格按以下顺序执行，不可跳过或调换步骤。

### 阶段 0：理解上下文 → 产品定型 → 需求分级

1. 完整阅读并理解用户提供的所有业务上下文。

2. 加载：
   - `references/framework/complexity-assessment.md`
   - `references/framework/global-checks/g1-product-type-fit.md`

3. 从用户描述中推断：
   - **商业属性**：商业化产品 or 企业自研系统
   - **功能类型**：业务管理型 / 工具型 / 交易平台型 / 基础服务型

4. 用一句话向用户呈现推断结果，请求确认：

   > 根据你的描述，这是一个【{商业属性} × {功能类型}】产品{，简要理由}。我会据此调整 PRD 各章节的侧重点。如有不对请纠正。

5. 等待用户确认后再继续。

6. **需求分级**：按 `complexity-assessment.md §1` 的四步法（先一句话用户视角描述 → 决策树 → 歧义消解 → 辅助信号）判定 L1 / L2 / L3 / L4。

7. 向用户确认需求级别：

   > 根据描述，这是一个 **L{X}（{级别名}）** 需求，我会生成 **{体量描述}** 的文档。如需调整深度请告诉我。

8. 等待用户确认。按 `complexity-assessment.md §3` 的章节适用表和 §4 的产品类型叠加规则，确定哪些章节需要生成、各章节深度到哪一层。

---

### 阶段 1：章节生成（按 L 级裁剪）

对当前 L 级适用的每一章，执行：

**Step 1** — 加载**质量标准**（写作目标）：
`references/framework/chapters/chN-*.md`

**Step 2** — 加载**生成指引**（模板/Mermaid/表格结构）：
`references/chapters/create-prd-chN-*.md`

**Step 3** — 写该章内容，必须命中 L 级对应的 Must 项，可覆盖 Should 项。写完立即输出。

**Step 4** — 完成该章后不再保留两个文件在上下文，进入下一章。

#### 章节顺序与适用性

按 `complexity-assessment.md §3` 的章节适用表裁剪。常见映射：

| L 级 | 需要生成的章节 |
|------|--------------|
| L1 | 变更说明（可套用 Ch10.2 配置级模板）+ 影响范围（Ch6 轻量）+ TBD |
| L2 | Ch1(简化)、Ch2(简化)、Ch6(轻量)、Ch10.1(流程图必需)、Ch10.2、Ch10.3、Ch14 |
| L3 | Ch1、Ch2、Ch6、Ch10.1-10.3、Ch11(可选)、Ch12(变更部分)、Ch13(上线+回滚)、Ch14 |
| L4 | 全量 Ch1-Ch14 |

**生成指引目录**（与 `prd-quality-framework/chapters/` 一一对应）：

1. Ch1  → `references/chapters/create-prd-ch01-background.md`
2. Ch2  → `references/chapters/create-prd-ch02-basic.md`
3. Ch3  → `references/chapters/create-prd-ch03-commercial.md`
4. Ch4  → `references/chapters/create-prd-ch04-goals.md`
5. Ch5  → `references/chapters/create-prd-ch05-overview.md`
6. Ch6  → `references/chapters/create-prd-ch06-scope.md`
7. Ch7  → `references/chapters/create-prd-ch07-risks.md`
8. Ch8-9 → `references/chapters/create-prd-ch08-09-terms.md`
9. Ch10 → `references/chapters/create-prd-ch10-functions.md` (含 10.1/10.2/10.3)
10. Ch11 → `references/chapters/create-prd-ch11-tracking.md`
11. Ch12 → `references/chapters/create-prd-ch12-permissions.md`
12. Ch13 → `references/chapters/create-prd-ch13-operations.md`
13. Ch14 → `references/chapters/create-prd-ch14-tbd.md`

---

### 阶段 2：自检（L3/L4 必做，L1/L2 跳过）

L3/L4 级别生成完毕后执行轻量自检：

**Step 1** — 加载 `references/framework/global-checks/g2-document-structure.md`，扫描：
- 章节覆盖是否与 L 级匹配
- **Ch1→Ch4→Ch10 逻辑链路是否贯通**（最核心）
- Ch10 内部三块（10.1/10.2/10.3）是否对齐
- Ch4→Ch11 目标是否都可度量
- Ch6→Ch12 角色/系统范围是否自洽
- 术语/角色名是否全文一致

**Step 2** — 加载 `references/framework/global-checks/g3-major-risks.md`，扫描 R1-R8 中的高严重度风险，在文末列出待完善清单。

自检输出写入 PRD 文末的"附：待完善清单"区域。

---

## 输出规范

### 文档格式

以单个 Markdown 文档输出 PRD，结构如下：

```md
# {产品/项目名称} PRD

| PRD 审核人 | {待填写} |
| --- | --- |
| 重要性 | {高/中/低} |
| 紧迫性 | {高/中/低} |
| 需求方 | {从上下文推断或标注待填写} |
| PRD 编写人 | {用户姓名或待填写} |
| PRD 提交日期 | {当前日期} |

## PRD 修改记录

| 变更时间 | 变更内容 | 变更提出部门与理由 | 修改人 | 审核人 | 版本号 |
| --- | --- | --- | --- | --- | --- |
| {当前日期} | 初始版本 | — | {编写人} | {待填写} | v1.0 |

---

## 1、项目背景
...（各章节内容）

## 14、待决事项
...

---

## 附：待完善清单
...（阶段 2 自检输出）
```

### 内容生成规则

1. **有信息则生成实质内容**：根据用户提供的上下文，尽可能生成具体、有实质内容的初稿。
2. **信息不足则标注 `[TODO]`**：对于用户未提供足够信息的部分，用 `[TODO: 具体需要补充什么]` 标注，而不是编造内容。
3. **按 L 级裁剪**：严格遵守章节适用表，不在低 L 级需求中过度设计。
4. **按产品类型调整**：商业化产品与企业自研系统的内容侧重点不同。
5. **质量标准对齐**：每章必须命中 `prd-quality-framework/chapters/chN-*.md` 对应 L 级的 **Must** 项。
6. **理论框架外显**：在关键章节中，用简短提示说明所使用的方法论框架（格式 `> 💡 方法论提示：`）。
7. **结构化优先**：表格、列表、Mermaid 图表优先于大段叙述。
8. **图表使用 Mermaid**：架构图、流程图、状态机、ER 模型等全部使用 Mermaid 代码块生成，不使用 ASCII 伪图。

### 图表生成规则

第10章产品框架概述中，以下图表**必须使用 Mermaid 语法**：

| 图表类型 | Mermaid 语法 | 必须包含 |
| --- | --- | --- |
| 应用架构图 | `graph TB` + `subgraph` 分层 | 用户层、接入层、业务服务层、数据层、外部系统 |
| ER 数据模型 | `erDiagram` | 所有核心实体+关系+关键属性（PK/FK/状态） |
| 业务流程图 | `flowchart TD` 或泳道 | 主流程+关键分支+异常路径 |
| 状态机图 | `stateDiagram-v2` | 正常+异常路径，附 note 说明约束 |

**注意事项：**
- Mermaid 图后面附对应的明细表格作为补充说明（如状态机图+状态转换表）
- 图表内节点文字用 `<br/>` 换行，保持简洁
- 具体模板和示例见第10章生成指引文件

### 逐章输出规则

- 每完成一章立即输出，不要等所有章节完成后再一起输出。
- 每章必须有清晰的章节标题，与 PRD 模板结构一致。
- 结构化数据（字段、权限、规则等）优先使用表格。
- 不确定的内容用 `[TODO]` 标注，并说明需要补充什么信息。

## 工作风格

- 目标是生成一份可用的 PRD 脚手架，加速产品经理的工作，而不是替代其判断。
- 用户上下文充分时，尽量具体和有实质内容；信息不足时，坦诚标注缺口。
- 保持专业的 PRD 写作风格：精确、结构化、无歧义。
- 根据用户提供的上下文丰富度调整深度——一段话的上下文生成轻量 PRD，详细上下文生成丰富 PRD。
- 如果用户提供的上下文非常有限，生成结构框架并附带指引说明，主动询问哪些补充信息有助于充实关键章节。
- **尊重渐进加载**：除非当前阶段需要，不要提前加载框架文件。
