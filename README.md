# Clash 共享分流规则

电脑与 iOS Clash 共用的规则地址。此仓库只维护规则文件和引用示例，不修改客户端，也不保存节点、订阅链接、公司内网域名或个人配置。

仓库：https://github.com/matoujin/clash-routing

## 使用地址

规则引用示例：

https://raw.githubusercontent.com/matoujin/clash-routing/main/examples/rule-providers.yaml

这个文件是配置片段，包含 `rule-providers` 和 `rules`，不是包含节点的完整机场订阅。将所需条目合并到自己的配置，策略组名称改为设备上实际使用的名称。已使用本次电脑分组命名的配置可直接复用示例中的目标名称。

自维护规则地址：

- Cursor：https://raw.githubusercontent.com/matoujin/clash-routing/main/rules/cursor.yaml
- Grok：https://raw.githubusercontent.com/matoujin/clash-routing/main/rules/grok.yaml
- 开发工具：https://raw.githubusercontent.com/matoujin/clash-routing/main/rules/development.yaml

通用分类位于 `rules/upstream/`，例如：

- AI：https://raw.githubusercontent.com/matoujin/clash-routing/main/rules/upstream/meta-ai.mrs
- 国内域名：https://raw.githubusercontent.com/matoujin/clash-routing/main/rules/upstream/meta-cn.mrs
- Google：https://raw.githubusercontent.com/matoujin/clash-routing/main/rules/upstream/meta-google.mrs

电脑和手机均需支持 Mihomo 风格的 `rule-providers`、`RULE-SET` 与 MRS。ProjectClash/Clash-Client 使用自己的 Clash 内核；此仓库提供标准配置片段，手机端仍应以实际安装版本的导入结果为准，不宣称已在真机验证。

## 更新方式

GitHub Actions 每天检查上游，有内容变化时提交到 `main`；也可手动运行工作流。设备按 `interval: 86400` 每 24 小时检查一次规则更新。首次需要下载，后续沿用客户端的本地缓存。仓库工作流和设备刷新是两个独立步骤，更新并非实时推送。

自维护规则修改发布后，电脑和手机在下一次规则更新时获取。GitHub 仓库本身不会修改设备上的策略组、DNS、节点或客户端。

## 分类和优先级

提供 AI、Google、GitHub、Apple、Microsoft、YouTube、Netflix、Spotify、Twitch、TikTok、Telegram、Discord、WhatsApp、Slack、Docker 和国内域名分类。

建议顺序：本地/公司例外 → Cursor/Grok 等自定义规则 → AI、通讯、影音等具体分类 → Google/Apple/Microsoft 等大分类 → 国内域名 → 最终兜底。已有的 IP 规则与兜底规则由设备自行保留。只加入实际需要的分类，避免多来源重复覆盖。

MRS 域名规则不包含所有 IP 直连流量；应用的 UDP、系统代理接管、账号地区限制也不由域名规则本身解决。

## 来源

- [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat)：通用域名分类，MRS 格式。
- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)：Docker 补充规则，保留原作者注释。
- `rules/cursor.yaml`、`rules/grok.yaml`、`rules/development.yaml`：本仓库维护的精确域名列表。

上游文件保留原内容，来源地址登记在 `sources.json`，权利与使用条件以原项目为准。
