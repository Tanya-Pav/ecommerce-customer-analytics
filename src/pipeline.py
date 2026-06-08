import os
import pandas as pd

class EcomDataPipeline:
    """__"""
    def __init__(self,input_path:str,output_path:str):
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    def load_data(self) -> pd.DataFrame:
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f'Input file {self.input_path} not found.')

        self.df = pd.read_csv(self.input_path, encoding= "ISO-8859-1")
        print( f"[УСПЕХ] Данные загружены. Исходный размер: {self.df.shape}")
        return self.df

    def clean_data(self) -> pd.DataFrame:
        """Проведение комплексной очистки данных от аномалий, дубликатов и пропусков."""
        if self.df is None:
            raise ValueError(
                "Данные не загружены. Сначала вызовите метод load_data()."
            )

        initial_rows = len(self.df)
        self.df = self.df.dropna(subset=["CustomerID"])
        print(
            f"[ОЧИСТКА] Удалено строк без CustomerID: {initial_rows - len(self.df)}"
        )

        self.df["CustomerID"] = self.df["CustomerID"].astype(int).astype(str)
        self.df["InvoiceDate"] = pd.to_datetime(self.df["InvoiceDate"])

        self.df["IsReturn"] = self.df["InvoiceNo"].str.startswith(
            "C", na=False
        )

        normal_transactions = (self.df["Quantity"] > 0) & (
                self.df["IsReturn"] == False
        )
        refund_transactions = (self.df["Quantity"] < 0) & (
                self.df["IsReturn"] == True
        )
        self.df = self.df[normal_transactions | refund_transactions]

        self.df = self.df[self.df["UnitPrice"] > 0]

        self.df["TotalPrice"] = self.df["Quantity"] * self.df["UnitPrice"]

        duplicate_count = self.df.duplicated().sum()
        self.df = self.df.drop_duplicates()
        print(f"[ОЧИСТКА] Удалено полных дубликатов строк: {duplicate_count}")

        print(f"[УСПЕХ] Очистка завершена. Новый размер: {self.df.shape}")
        return self.df

    def save_processed_data(self):
        """Сохранение очищенных данных в директорию processed/."""
        if self.df is None:
            raise ValueError("Нет данных для сохранения.")

        os.makedirs(os.path.dirname(self.output_path), exist_ok=True)
        self.df.to_csv(self.output_path, index=False)
        print(f"[УСПЕХ] Очищенные данные сохранены в: {self.output_path}")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    INPUT_FILE = os.path.join(project_root, "data", "raw", "OnlineRetail.csv")
    OUTPUT_FILE = os.path.join(project_root, "data", "processed", "cleaned_ecommerce_data.csv")

    pipeline = EcomDataPipeline(input_path=INPUT_FILE, output_path=OUTPUT_FILE)
    pipeline.load_data()
    pipeline.clean_data()
    pipeline.save_processed_data()