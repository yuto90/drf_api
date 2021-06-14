from django.db import models
# AbstractBaseUserを利用してUserモデルをカスタマイズ
from django.contrib.auth.models import AbstractBaseUser
# PermissionsMixinを用いてUserの認証を行う
from django.contrib.auth.models import PermissionsMixin
# BaseUserManager利用してUserManagerモデルをカスタマイズ
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ カスタムユーザーマネージャー """

    # ユーザを作成するメソッド
    def create_user(self, email, name, password=None):
        """ ユーザー作成 """

        if not email:
            raise ValueError('User must have an email address')

        # emailのドメインを小文字に変換
        email = self.normalize_email(email)

        # UserProfileモデルを参照してuserを定義
        user = self.model(email=email, name=name)

        # userが入力したパスワードをハッシュ化
        user.set_password(password)

        # settings.pyでdefaultに設定されているDBに保存
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """ スーパーユーザー作成 """

        # 上記create_userを利用
        user = self.create_user(email, name, password)

        # superuserの権限を適用
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ カスタムユーザーモデル """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    # ユーザが退会したらfalseにして論理削除
    is_active = models.BooleanField(default=True)

    # 管理画面にアクセスを許可するか
    is_staff = models.BooleanField(default=False)

    # UserProfileManagerのメソッドを使えるようにする
    objects = UserProfileManager()

    # emailを利用したログイン認証に変更
    USERNAME_FIELD = 'email'

    # 必須項目追加
    REQUIRED_FIELDS = ['name']

    # 1つのnameフィールドで表示したいので、既存のメソッドをオーバーライド
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    # 管理画面などで表示される文字列を定義
    def __str__(self):
        return self.email


class Blog(models.Model):
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    # 外部キー
    author = models.ForeignKey(
        UserProfile, related_name='blogs', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
