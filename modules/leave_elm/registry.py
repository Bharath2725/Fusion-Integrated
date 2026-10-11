NAV_ITEMS = [
    {"code": "leave.mine", "label": "My Leaves", "icon": "ClipboardText", 
     "to": "/leave/mine", "required_permission": "leave_elm.application.view_self", "sort_order": 10},
    {"code": "leave.apply", "label": "Apply for Leave", "icon": "Signature", 
     "to": "/leave/apply", "required_permission": "leave_elm.application.apply", "sort_order": 20},
    {"code": "leave.approvals", "label": "Approvals", "icon": "Checks", 
     "to": "/leave/approvals", "required_permission": "leave<｜begin▁of▁sentence｜>leave_elm.application.review