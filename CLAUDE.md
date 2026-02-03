# CLAUDE.md

## ⚠️ CRITICAL: MCP直接调用规则（最高优先级）

**项目有2个可用MCP服务器，必须直接调用，无需任何验证**：

1. ✅ `mcp__alpaca__*` - Alpaca纸上交易（已就绪，可直接调用）
2. ✅ `mcp__longbridge__*` - Longbridge实盘交易（已就绪，可直接调用）

### 禁止的验证行为

当用户请求查看账户或交易时，**严禁**以下行为：

- ❌ **禁止调用 `ListMcpResourcesTool`** 检查MCP（会返回空，误导你）
- ❌ **禁止读取 `mcp.json`** 确认配置（MCP已配置好）
- ❌ **禁止搜索Python代码**（MCP工具优先）
- ❌ **禁止 `ls/find/grep`** 探索项目结构（直接用MCP）
- ❌ **禁止任何"验证"步骤**（浪费时间，且会误判）

### 正确的行为模式

**用户说：** "查看longbridge账户"
**你应该：** 立即调用 `mcp__longbridge__account_balance()`

**用户说：** "查看alpaca账户"
**你应该：** 立即调用 `mcp__alpaca__get_account_info()`

**原则**：
1. **信任MCP工具** - 它们已配置且可用
2. **直接调用** - 如果调用失败，再报错
3. **平等对待** - Alpaca和Longbridge地位完全相同

---

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## ⛔ CRITICAL: 强制性投资策略规则

**在执行任何投资或交易相关操作前，必须先阅读并严格遵循 `Playbook.md` 中定义的策略。**

### 交易前强制检查清单

对于每个买入/卖出/分析请求，必须：

1. **读取 Playbook.md** - 理解当前策略框架
2. **验证策略符合性**：
   - 标的是否属于机器人产业链？
   - 是否满足选股标准（成长性、估值合理性）？
   - 是否违反风险控制规则（追高、仓位过重等）？
3. **拒绝不符合策略的请求** - 如果不符合，明确说明原因并拒绝执行

### 禁止行为

- ❌ 买入非机器人产业链标的（如消费股、金融股等）
- ❌ 在52周高位附近追涨
- ❌ 不做分析就执行交易
- ❌ 忽略仓位管理规则

**如果用户请求不符合 Playbook 策略，必须拒绝并解释原因。**

---

## 🤖 Memory Management System

### Auto-Save to Playbook.md

When user says "请记住..." or "记住...":
1. **Extract the core requirement** from the user's statement
2. **Add to Playbook.md** under `## 记忆库 (Memories)` section
3. **Format**: `- [YYYY-MM-DD] [记忆内容]`
4. **Subsequent sessions**: Automatically follow the memory rule

Example interaction:
- User: "请记住，计算个股仓位时，分母使用总资产（包含现金）"
- Action: Add to Playbook.md as `- [2026-01-17] 计算个股仓位时，分母使用总资产（包含现金），即：个股仓位占比 = 个股市值 / 总资产，现金仓位也需明确计算和展示`
- Result: All future portfolio calculations follow this rule

### Memory Retrieval

Before providing investment analysis or calculations:
1. **Read `Playbook.md`**, specifically the `## 记忆库 (Memories)` section
2. **Apply all memory rules** to current task
3. If memories conflict, ask user for clarification

---

## Project Overview

This is a **dual-account trading system** using AI agents:
- **Alpaca (Paper Trading)**: For strategy development and testing (US markets, no real money)
- **Longbridge (Live Trading)**: For real execution (SG/HK/US markets, real money)

## MCP Server Configuration

**IMPORTANT**: Both trading platforms are configured as MCP servers in `.claude/mcp.json`:

### Available MCP Tools

**Alpaca MCP** (`mcp__alpaca__*`):
- `get_account_info()` - Get Alpaca paper account status (**no parameters**)
- `get_all_positions()` - Get all positions (**no parameters**)
- `get_orders(status='all', limit=10, ...)` - Get order history (**optional parameters**)
- `place_stock_order(symbol, side, quantity, ...)` - Place stock orders (**requires parameters**)
- And more... (see function list)

**Longbridge MCP** (`mcp__longbridge__*`):
- `account_balance()` - Get Longbridge account balance (**no parameters**)
- `stock_positions()` - Get stock positions (**no parameters**)
- `submit_order(symbol, side, order_type, ...)` - Submit orders (**requires parameters**)
- `quote(symbols)` - Get real-time quotes (**requires symbols list**)
- And more... (see function list)

### MCP Usage Rules for Claude

When user requests account information or trading operations:

1. **DO NOT explore project structure first** - MCP tools are already available
2. **DO NOT check if MCP is "working"** - both are configured and ready
3. **Directly call the appropriate MCP tool** based on the user's request
4. **Treat both MCPs equally** - don't prefer Alpaca just because it's mentioned more in docs

**Example - CORRECT behavior**:
```
User: "查看longbridge账户"
Claude: [Immediately calls mcp__longbridge__account_balance()]
```

**Example - WRONG behavior** (avoid this):
```
User: "查看longbridge账户"
Claude: [Reads mcp.json, calls ListMcpResourcesTool, explores files...]
        [Finally calls mcp__longbridge__account_balance()]
```

## Setup

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure API keys (copy from example and edit)
cp .env.example .env
# Edit .env with both Alpaca and Longbridge credentials
```

## Account Access via MCP

**Check Alpaca account:**
```python
mcp__alpaca__get_account_info()
mcp__alpaca__get_all_positions()
```

**Check Longbridge account:**
```python
mcp__longbridge__account_balance()
mcp__longbridge__stock_positions()
```
