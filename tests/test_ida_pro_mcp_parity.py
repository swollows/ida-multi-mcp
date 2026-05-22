"""Static coverage checks for ida-pro-mcp parity additions."""

from ida_multi_mcp.server import _load_static_ida_tools


def test_upstream_parity_tools_are_advertised_without_ida():
    tool_names = {tool["name"] for tool in _load_static_ida_tools()}
    expected = {
        "entity_query",
        "search_text",
        "py_exec_file",
        "make_signature",
        "make_signature_for_function",
        "make_signature_for_range",
        "find_xref_signatures",
        "type_query",
        "type_inspect",
        "type_apply_batch",
    }

    assert expected <= tool_names
