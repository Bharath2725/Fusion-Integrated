MODULE = {
    "code": "leave_elm", 
    "label": "Leave Management", 
    "icon": "CalendarBlank", 
    "base_path": "/leave", 
    "nav_section": "Leave", 
    "sort_order": 20, 
    "status": "active"
}

PERMISSIONS = [
    ("leave_elm.application.apply", "Submit a leave application"),
    ("leave_elm.application.view_self", "See own leave applications"),
    ("leave_elm.application.withdraw", "Withdraw a pending application"),
    ("leave_elm.application.cancel", "Request cancellation of approved leave"),
    ("leave_elm.application.extend", "Request extension of ongoing leave"),
    ("leave_elm.application.resume", "Submit resumption of duty"),
    ("leave_elm.substitute.respond", "Accept or decline substitute assignment"),
    ("leave_elm.application.review", "Recommend or not recommend a request"),
    ("leave_elm.application.sanction", "Approve or reject a request"),
    ("leave_elm.balance.view_self", "See own leave balances"),
    ("leave_elm.policy.manage", "Maintain leave policy parameters"),
    ("leave_elm.calendar.manage", "Maintain holiday calendar"),
    ("leave_elm.record.manage", "Record offline-sanctioned leave")
]
