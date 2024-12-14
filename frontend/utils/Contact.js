export default class Contact {
  constructor(name, position, department, office, office_phone, mobile_phone, level, leader) {
    this.name = name; // 姓名
    this.position = position; // 职位
    this.department = department; // 科室
    this.office = office; // 办公室
    this.office_phone = office_phone; // 办公电话
    this.mobile_phone = mobile_phone; // 手机
    this.level = level; // 级别
    this.leader = leader; // 分管领导
  }

  toJSON() {
    return {
      name: this.name,
      position: this.position,
      department: this.department,
      office: this.office,
      office_phone: this.office_phone,
      mobile_phone: this.mobile_phone,
      level: this.level, // 级别
      leader: this.leader // 分管领导
    };
  }
}
