# Changelog

## v1.1 (2026-05-17)

### 社区扩展分支

- 新增社区扩展分支 [`community/c-end-product`](https://github.com/pmYangKun/create-prd-skill/tree/community/c-end-product)，由 [@s2dongman](https://github.com/s2dongman)（申悦）贡献，把 B 端 PRD 生成 prompt 全面改造为 C 端版本（产品定型、商业分析、目标体系、MVP、功能需求、埋点、权限、运营全部切换为 C 端视角），含 `dist/create-cprd-universal-prompt.md`（1683 行）
- README 社区贡献章节重写为三分支并列（main / complexity-aware / c-end-product），补充 C 端版的详细改造点和切换命令

## v1.0 (2026-04-02)

- 初始版本
- 14 章结构化 PRD 生成，支持逐章即时输出
- 产品定型机制（商业化产品 vs 企业自研系统 × 四种功能类型）
- 基于《决胜B端》《决胜体验设计》《决胜B端PRD模板v2.0》构建
- 生成后自动执行轻量自检，输出待完善清单
- 支持 Claude Code skill 集成和任意大模型通用 prompt
