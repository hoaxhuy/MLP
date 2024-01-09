from minio import Minio
from minio.error import S3Error

def upload_to_minio(minio_endpoint, access_key, secret_key, bucket_name, file_path, object_name):
    # Khởi tạo client MinIO
    minio_client = Minio(
        minio_endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=False  # Đặt thành True nếu sử dụng kết nối an toàn (HTTPS)
    )

    try:
        # Kiểm tra xem bucket đã tồn tại chưa, nếu không thì tạo mới
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        # Tải file lên MinIO
        minio_client.fput_object(bucket_name, object_name, file_path)

        print(f"File {object_name} đã được tải lên thành công lên bucket {bucket_name}")

    except S3Error as e:
        print(f"Lỗi khi tải lên file lên MinIO: {e}")

if __name__ == "__main__":
    minio_endpoint = "http://127.0.0.1:9000"  # Điền địa chỉ MinIO server
    access_key = "FlFBRgc17cH2vWdjTamd"
    secret_key = "LVJaTYCNxIZqtDNpIu3wXujW7nLIPqboGeQ79ofA"
    bucket_name = "File-server"
    file_path = "/home/mac-pro/Downloads/Corona_NLP_test.csv"  # Đường dẫn đến file cần tải lên
    object_name = "Corona.csv"  # Tên đối tượng trong MinIO

    upload_to_minio(minio_endpoint, access_key, secret_key, bucket_name, file_path, object_name)
