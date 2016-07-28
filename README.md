# pic4pic

一个用小图生成大图的脚本。

#### 使用方法
1. img目录下放尽量多的小图，小图尽量统一大小
2. 把需要生成的源图拷贝到主目录，并替换掉`big.jpg`
3. 运行 `main.py`,windows直接双击`run.bat`

第一次运行会生成pathes.txt文件，记录小图的颜色  

	F:\_ldw\pic4pic>python main.py
	create color table: 100%
	paste img: 100%

如果更新了`img`目录，删除掉`pathes.txt`文件，再运行。

#### 生成效果
源图片  
![](big.jpg)

使用800个小图作为数据后，生成的效果：  
![](bigout.jpg)
