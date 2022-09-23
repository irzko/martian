from random import randint
from tkinter import W
from bs4 import BeautifulSoup as bs
import json
import io


class Name:
    def __init__(self, *fullname):
        self.fullname = fullname

    def __str__(self):
        return " ".join(self.fullname)


class NameGenerator:
    LAST_NAME = ['Họ', 'Nguyễn', 'Trần', 'Lê', 'Phạm', 'Huỳnh', 'Hoàng', 'Võ', 'Vũ', 'Phan', 'Trương', 'Bùi', 'Đặng', 'Đỗ', 'Ngô', 'Hồ', 'Dương', 'Đinh', 'Đoàn', 'Lâm', 'Mai', 'Trịnh', 'Đào', 'Cao', 'Lý', 'Hà', 'Lưu', 'Lương', 'Thái', 'Châu', 'Tạ', 'Phùng', 'Tô', 'Vương', 'Văn', 'Tăng', 'Quách', 'Lại', 'Hứa', 'Thạch', 'Diệp', 'Từ', 'Chu', 'La', 'Đàm', 'Tống', 'Giang', 'Chung', 'Triệu', 'Kiều', 'Hồng', 'Trang', 'Đồng', 'Danh', 'Lư', 'Lữ', 'Thân', 'Kim', 'Mã', 'Bạch', 'Liêu', 'Tiêu', 'Dư', 'Bành', 'Âu', 'Tôn', 'Khưu', 'Sơn', 'Tất', 'Nghiêm', 'Lục', 'Quan', 'Phương', 'Mạc', 'Lai', 'Vòng', 'Mạch', 'Thiều', 'Trà', 'Đậu', 'Nhan', 'Lã', 'Trình', 'Ninh', 'Vi', 'Biện', 'Hàng', 'Ôn', 'Chế', 'Nhâm', 'Tôn Nữ', 'Thi', 'Doãn', 'Khổng', 'Phù', 'Đường', 'Ông', 'Tôn Thất', 'Ngụy', 'Viên', 'Tào', 'Cù', 'Kha']
    ST_FEMALE_MIDDLE_NAME = ['Thị', 'Ngọc', 'Nguyễn', 'Hoàng', 'Lê', 'Trần', 'Thanh', 'Bảo', 'Phương', 'Huỳnh', 'Gia', 'Minh', 'Kim', 'Quỳnh', 'Phạm', 'Khánh', 'Hồng', 'Mỹ', 'Hà', 'Vũ', 'Võ', 'Mai', 'Thùy', 'Anh', 'Như', 'Thảo', 'Thụy', 'Phan', 'Yến', 'Đặng', 'Xuân', 'Hồ', 'Thiên', 'Đỗ', 'Nhật', 'Thái', 'Tường', 'Tuyết', 'Nhã', 'Thúy', 'Dương', 'Hải', 'Thu', 'Lâm', 'Trúc', 'Trương', 'Hoài', 'Đoàn', 'Ngô', 'Tú', 'Cao', 'Kiều', 'Ánh', 'Phúc', 'Bích', 'Châu', 'Bùi', 'Khả', 'Vân', 'Đình', 'Tâm', 'Thục', 'Bội', 'Ái', 'Lý', 'Hương', 'Nguyên', 'Uyên', 'Thủy', 'Trịnh', 'Cẩm', 'Đào', 'Diệp', 'Tuệ', 'Diệu', 'Huệ', 'Diễm', 'Lan', 'Cát', 'Huyền', 'An', 'Linh', 'Lưu', 'Quế', 'Ngân', 'Đinh', 'Uyển', 'Triệu', 'Trà', 'Song', 'Bình', 'Nguyệt', 'Trang', 'Mẫn', 'Kỳ', 'Trâm', 'Hạnh', 'Lương', 'Vương', 'Tiểu']
    ST_MALE_MIDDLE_NAME = ['Minh', 'Hoàng', 'Gia', 'Nguyễn', 'Quốc', 'Thanh', 'Văn', 'Thành', 'Anh', 'Ngọc', 'Tấn', 'Đức', 'Lê', 'Tuấn', 'Quang', 'Trần', 'Hữu', 'Nhật', 'Duy', 'Trọng', 'Đình', 'Đăng', 'Huỳnh', 'Trung', 'Bảo', 'Phúc', 'Tiến', 'Chí', 'Thiên', 'Công', 'Xuân', 'Phạm', 'Vũ', 'Thái', 'Huy', 'Võ', 'Hải', 'Thế', 'Hồng', 'Khánh', 'Trí', 'Phước', 'Phú', 'Nguyên', 'Việt', 'Mạnh', 'Bá', 'Trường', 'Vĩnh', 'Hoài', 'Phan', 'Cao', 'Đặng', 'Hồ', 'Dương', 'Thiện', 'Lâm', 'Kim', 'Đỗ', 'Trương', 'Đại', 'Viết', 'Phi', 'Phương', 'Nam', 'Đoàn', 'Hà', 'Kiến', 'Ngô', 'Nhựt', 'Hiếu', 'Bùi', 'An', 'Hùng', 'Chấn', 'Bình', 'Khải', 'Khắc', 'Khôi', 'Mai', 'Châu', 'Sỹ', 'Vĩ', 'Tùng', 'Lý', 'Long', 'Hưng', 'Hạo', 'Phát', 'Như', 'Đinh', 'Quý', 'Đắc', 'Vinh', 'Nhất', 'Đông', 'Lương', 'Kỳ', 'Trịnh', 'Thuận']
    ND_FEMALE_MIDDLE_NAME = ['Bảo', 'Ngọc', 'Phương', 'Thanh', 'Minh', 'Kim', 'Quỳnh', 'Khánh', 'Như', 'Thảo', 'Anh', 'Yến', 'Gia', 'Mỹ', 'Thùy', 'Hồng', 'Tường', 'Thiên', 'Hoàng', 'Thu', 'Tuyết', 'Trúc', 'Mai', 'Xuân', 'Thúy', 'Bích', 'Cẩm', 'Ánh', 'Kiều', 'Diễm', 'Hà', 'Lan', 'Hải', 'Thủy', 'Nhã', 'Vân', 'Trâm', 'Trà', 'Tú', 'Cát', 'Uyên', 'Hoài', 'Huyền', 'Huỳnh', 'Linh', 'Nhật', 'Hương', 'Tâm', 'An', 'Diệu', 'Ái', 'Ngân', 'Đan', 'Khả', 'Kỳ', 'Thị', 'Quế', 'Tố', 'Đông', 'Thái', 'Song', 'Nam', 'Phi', 'Hạnh', 'Ý', 'Thục', 'Phúc', 'Châu', 'Tuệ', 'Uyển', 'Nguyệt', 'Đoan', 'Lê', 'Nguyên', 'Mộng', 'Bình', 'Trang', 'Lam', 'Hiền', 'Băng', 'Mẫn', 'Thụy', 'Vy', 'Hạ', 'Việt', 'Hiếu', 'Triệu', 'Trường', 'Lệ', 'Phượng', 'Diệp', 'Lâm', 'Thy', 'Bé', 'Yên', 'Khải', 'Tiểu', 'Huệ', 'Phước', 'Đỗ']
    ND_MALE_MIDDLE_NAME = ['Minh', 'Gia', 'Anh', 'Hoàng', 'Quốc', 'Bảo', 'Tuấn', 'Thiên', 'Đăng', 'Thanh', 'Nhật', 'Thành', 'Duy', 'Tấn', 'Đức', 'Phúc', 'Quang', 'Khánh', 'Trung', 'Hải', 'Ngọc', 'Trọng', 'Huy', 'Thái', 'Hữu', 'Tiến', 'Nguyên', 'Trường', 'Trí', 'Phú', 'Phước', 'Hoài', 'An', 'Nam', 'Việt', 'Phương', 'Xuân', 'Chí', 'Thế', 'Phi', 'Khôi', 'Công', 'Thiện', 'Hồng', 'Vĩnh', 'Bình', 'Đình', 'Đại', 'Lê', 'Mạnh', 'Hiếu', 'Văn', 'Nhựt', 'Kim', 'Vũ', 'Kỳ', 'Long', 'Bá', 'Đông', 'Hùng', 'Hưng', 'Khang', 'Cao', 'Kiến', 'Sơn', 'Nhất', 'Tùng', 'Phát', 'Lâm', 'Khải', 'Thuận', 'Tâm', 'Hạo', 'Nhân', 'Triệu', 'Vinh', 'Chấn', 'Tường', 'Phong', 'Quý', 'Nguyễn', 'Như', 'Huỳnh', 'Song', 'Thịnh', 'Triều', 'Châu', 'Vương', 'Tuần', 'Sỹ', 'Tài', 'Hà', 'Hoàn', 'Khắc', 'Linh', 'Toàn', 'Tần', 'Viết', 'Hòa', 'Bách']
    FEMALE_FIRST_NAME = ['Anh', 'Vy', 'Ngọc', 'Nhi', 'Hân', 'Thư', 'Linh', 'Như', 'Ngân', 'Phương', 'Thảo', 'My', 'Trân', 'Quỳnh', 'Nghi', 'Trang', 'Trâm', 'An', 'Thy', 'Châu', 'Trúc', 'Uyên', 'Yến', 'Ý', 'Tiên', 'Mai', 'Hà', 'Vân', 'Nguyên', 'Hương', 'Quyên', 'Duyên', 'Kim', 'Trinh', 'Thanh', 'Tuyền', 'Hằng', 'Dương', 'Chi', 'Giang', 'Tâm', 'Lam', 'Tú', 'Ánh', 'Hiền', 'Khánh', 'Minh', 'Huyền', 'Thùy', 'Vi', 'Ly', 'Dung', 'Nhung', 'Phúc', 'Lan', 'Phụng', 'Ân', 'Thi', 'Khanh', 'Kỳ', 'Nga', 'Tường', 'Thúy', 'Mỹ', 'Hoa', 'Tuyết', 'Lâm', 'Thủy', 'Đan', 'Hạnh', 'Xuân', 'Oanh', 'Mẫn', 'Khuê', 'Diệp', 'Thương', 'Nhiên', 'Băng', 'Hồng', 'Bình', 'Loan', 'Thơ', 'Phượng', 'Mi', 'Nhã', 'Nguyệt', 'Bích', 'Đào', 'Diễm', 'Kiều', 'Hiếu', 'Di', 'Liên', 'Trà', 'Tuệ', 'Thắm', 'Diệu', 'Quân', 'Nhàn', 'Doanh']
    MALE_FIRST_NAME = ['Huy', 'Khang', 'Bảo', 'Minh', 'Phúc', 'Anh', 'Khoa', 'Phát', 'Đạt', 'Khôi', 'Long', 'Nam', 'Duy', 'Quân', 'Kiệt', 'Thịnh', 'Tuấn', 'Hưng', 'Hoàng', 'Hiếu', 'Nhân', 'Trí', 'Tài', 'Phong', 'Nguyên', 'An', 'Phú', 'Thành', 'Đức', 'Dũng', 'Lộc', 'Khánh', 'Vinh', 'Tiến', 'Nghĩa', 'Thiện', 'Hào', 'Hải', 'Đăng', 'Quang', 'Lâm', 'Nhật', 'Trung', 'Thắng', 'Tú', 'Hùng', 'Tâm', 'Sang', 'Sơn', 'Thái', 'Cường', 'Vũ', 'Toàn', 'Ân', 'Thuận', 'Bình', 'Trường', 'Danh', 'Kiên', 'Phước', 'Thiên', 'Tân', 'Việt', 'Khải', 'Tín', 'Dương', 'Tùng', 'Quý', 'Hậu', 'Trọng', 'Triết', 'Luân', 'Phương', 'Quốc', 'Thông', 'Khiêm', 'Hòa', 'Thanh', 'Tường', 'Kha', 'Vỹ', 'Bách', 'Khanh', 'Mạnh', 'Lợi', 'Đại', 'Hiệp', 'Đông', 'Nhựt', 'Giang', 'Kỳ', 'Phi', 'Tấn', 'Văn', 'Vương', 'Công', 'Hiển', 'Linh', 'Ngọc', 'Vĩ']
    
    def __init__(self, gender):
        if gender == 'random':
            g = randint(1, 2)
            if g == 1: self.gender = 'female'
            else: self.gender = 'male'
        else:
            self.gender = gender

    def get_last_name(self):
        return self.LAST_NAME[randint(0, len(self.LAST_NAME ) - 1)]

    def get_first_name(self):
        if self.gender == 'male':
            return self.MALE_FIRST_NAME[randint(0, len(self.MALE_FIRST_NAME) - 1)]
        elif self.gender == 'female':
            return self.FEMALE_FIRST_NAME[randint(0, len(self.FEMALE_FIRST_NAME) - 1)]

    def get_middle_name(self, amount_middle_name = randint(1, 2)):
        if self.gender == 'female':
            if (amount_middle_name == 1):
                return self.ST_FEMALE_MIDDLE_NAME[randint(0, len(self.ST_FEMALE_MIDDLE_NAME) - 1)]
            if (amount_middle_name == 2):
                return self.ST_FEMALE_MIDDLE_NAME[randint(0, len(self.ST_FEMALE_MIDDLE_NAME) - 1)] + ' ' + self.ND_FEMALE_MIDDLE_NAME[randint(0, len(self.ND_FEMALE_MIDDLE_NAME) - 1)]
        if self.gender == 'male':
            if (amount_middle_name == 1):
                return self.ST_MALE_MIDDLE_NAME[randint(0, len(self.ST_MALE_MIDDLE_NAME) - 1)]
            if (amount_middle_name == 2):
                return self.ST_MALE_MIDDLE_NAME[randint(0, len(self.ST_MALE_MIDDLE_NAME) - 1)] + ' ' + self.ND_MALE_MIDDLE_NAME[randint(0, len(self.ND_MALE_MIDDLE_NAME) - 1)]

    def get_full_name(self, middleName=True):
        if middleName:
            return Name(self.get_last_name(), self.get_middle_name(), self.get_first_name())
        else:    
            return Name(self.get_last_name(), self.get_first_name())
    def get_gender(self):
        if self.gender == 'female':
            return 'Nữ'
        else: return 'Nam'


# response = requests.get("https://hoten.org/dem-pho-bien-o-nam-gioi/")
# soup = bs(response.text, 'html.parser')
# table = soup.find_all('tr')
# name = []


# for i in range(len(table)):
#     name.append(table[i].find_all('td')[1].text.strip())


class Location:
    def __init__(self, country, city, district, ward, street):
        self.country = country
        self.city = city
        self.district = district
        self.ward = ward
        self.street = street

    def __str__(self):
        return ",".join([self.country, self.city, self.district, self.ward, self.street])
    


f = open('local.json', 'r', encoding='utf-8')
data = json.load(f)

def random_location():
    city = data[randint(0, len(data) - 1)]
    districts = city['districts']
    district = districts[randint(0, len(districts) - 1)]
    try:
        wards = district['wards']
        ward = wards[randint(0, len(wards) - 1)]
    except:
        ward = {"name": ""}

    try:
        streets = district['streets']
        street = streets[randint(0, len(streets) - 1)]
    except:
        street = {"name": ""}
    return Location('Việt Nam', city['name'].strip(), district['name'].strip(), ward['name'].strip(), street['name'].strip())



for i in range(12215):
    name_gen = NameGenerator('random')
    fullname = name_gen.get_full_name().__str__()
    gender = name_gen.get_gender()
    location = random_location().__str__()
    info = fullname + ',' + gender + ',' + location + '\n'
    f = io.open('demo.csv', 'a', encoding='utf8')
    f.write(info)
    f.close

