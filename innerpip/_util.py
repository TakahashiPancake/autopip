"""
Copyright (c) 2026 Yidong Zhu

Licensed under MIT

"""
import sys
from typing import Callable, Any

def del_module_by_name(module_name: str) -> Callable:
  """
  装饰器

  - 根据模块名称删除模块

  Args:
    module_name: 模块名称

  """
  def decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
      # 执行方法
      result = func(*args, **kwargs)
      # 移除模块
      if module_name in sys.modules:
        del sys.modules[module_name]
      return result
    return wrapper
  return decorator

