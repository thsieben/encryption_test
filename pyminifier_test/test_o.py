import os,sys
ޅ=bool
𐡁=Exception
ࡈ=True
𧃐=None
𧂶=range
𐲐=str
ࠕ=False
𐩸=sys.platform
ﲂ=os.chmod
ڨ=os.mkdir
𐢈=os.makedirs
𨭹=os.path
import pytest
ﴍ=pytest.main
𐤋=pytest.mark
뵿=pytest.raises
import tempfile
𪈭=tempfile.mkdtemp
import shutil
𐤁=shutil.rmtree
import stat
𪿄=stat.S_IROTH
𗁇=stat.S_IRGRP
懩=stat.S_IREAD
from go_drive.util import fs_util,appdirs,temp_utils
𠹋=temp_utils.make_random_name
𞢂=temp_utils.make_temporary_file
𦻃=appdirs.get_temp_dir
ࢱ=fs_util.serialize_filename
ݮ=fs_util.is_file_open_by_another_application
𐪏=fs_util.get_list_of_files_and_folders_in_tree
뙭=fs_util.remove_read_only_files
脃=fs_util.make_executable
𐫆=fs_util.rmtree
𣜠=fs_util.copy_tree
𢻴=fs_util.rename_folder
ﺒ=fs_util.backup_folder
尢=fs_util.rename_file
𤜉=fs_util.copy_file
ﶚ=fs_util.remove_child_files_and_folders
𞹒=fs_util.remove_file
ﲙ=fs_util.replace_folder
𨇾=fs_util.copy_to_temp_folder
𘉘=ޅ(𐩸=='darwin')
𦗵=𐩸.startswith('win')
def 𤿡():
 with 뵿(𐡁):
  𨇾()
 with 뵿(𐡁):
  𨇾("gibberish_path.txt")
 ܜ=𨇾(__file__,suffix=".txt")
 assert 𨭹.exists(ܜ)
def ڏ():
 assert not ﲙ("blah","",ࡈ)
 with 뵿(𐡁):
  ﲙ("gibberish_path.txt","")
 泠=𦻃()
 㠨=𪈭(prefix="replace_folder_dest_",dir=泠)
 𐢈(㠨+"/dest_folder1/dest_folder2")
 ﰌ=𪈭(prefix="replace_folder_src_",dir=泠)
 斏=𨭹.join(ﰌ,"src")
 𐢈(斏+"/src_folder1/src_folder2")
 ﲙ(斏,㠨)
 𞺻=𨭹.normpath(㠨+".bak")
 assert not 𨭹.exists(斏)
 assert 𨭹.exists(㠨+"/src_folder1/src_folder2")
 assert not 𨭹.exists(𞺻)
 𐤁(ﰌ)
 𐤁(㠨)
 assert not 𨭹.exists(㠨)
 assert not 𨭹.exists(ﰌ)
def 𞡱():
 assert 𞹒(𧃐)is 𧃐
def ﳲ():
 泠=𦻃()
 for i in 𧂶(10):
  𗝢=泠+"/"+𐲐(i)
  ڨ(𗝢)
  𢕛=𨭹.join(泠,𗝢)
  𐨐=""
  if i%2==0:
   㐴=𞢂("notes",dir=𗝢)
   𐨐=𨭹.join(𢕛,㐴)
   assert 𨭹.isfile(𐨐)
  else:
   assert not 𨭹.isfile(𐨐)
  if i%3==0:
   ﶚ(泠)
   assert not 𨭹.exists(𢕛)
   assert not 𨭹.isfile(𐨐)
  else:
   assert 𨭹.exists(𢕛)
def 钏():
 泠=𦻃()
 𥮴=𞢂("test",dir=泠)
 𠋌=𞢂("boo",dir=泠)
 with 뵿(𐡁):
  𤜉(𧃐,"blah")
 with 뵿(𐡁):
  𤜉("source",𧃐)
 with 뵿(𐡁):
  𤜉("source","dest")
 with 뵿(𐡁):
  𤜉(泠,泠+"/dest",ࠕ)
 𤜉(𥮴,𠋌)
def 䅉():
 泠=𦻃()
 𥮴=𞢂("test",dir=泠)
 𠋌=𞢂("boo",dir=泠)
 with 뵿(𐡁):
  尢(𧃐,"blah")
 with 뵿(𐡁):
  尢("source",𧃐)
 with 뵿(𐡁):
  尢("source","dest")
 with 뵿(𐡁):
  尢(泠,泠+"/dest",ࠕ)
 尢(𥮴,𠋌)
def 𩈀():
 泠=𦻃()
 𞤾=泠+".bak"
 ڨ(𞤾)
 𝘇=𞢂("test",dir=泠)
 with 뵿(𐡁):
  ﺒ(𧃐)
 with 뵿(𐡁):
  ﺒ(𝘇)
 with 뵿(𐡁):
  ﺒ(泠,".bak",ࠕ)
 𐪒=ﺒ(泠,".bak")
 𐣧=ﺒ(泠)
 pass
def ܞ():
 泠=𦻃()
 𞤾=泠+𠹋(5)
 ڨ(𞤾)
 𐦋=𞢂("test",dir=𞤾)
 with 뵿(𐡁):
  𢻴(𧃐,"dest")
 with 뵿(𐡁):
  𢻴(泠,𧃐)
 with 뵿(𐡁):
  𢻴("fake_path/fake",𞤾)
 with 뵿(𐡁):
  𢻴(泠,𐦋)
 with 뵿(𐡁):
  𢻴(泠,𞤾,ࠕ)
 𢻴("fake_path/fake",𞤾,ignore_empty_src=ࡈ)
 𢻴(泠,𞤾)
def 릸():
 泠=𦻃()
 𞤾=泠+𠹋(5)
 ﲅ=泠+𠹋(5)
 ㅜ=𨭹.join(ﲅ,𠹋(3))
 ڨ(𞤾)
 𝘇=𞢂("test",dir=泠)
 with 뵿(𐡁):
  𣜠(𧃐,"dest")
 with 뵿(𐡁):
  𣜠(泠,𧃐)
 with 뵿(𐡁):
  𣜠("source","dest")
 with 뵿(𐡁):
  𣜠(𝘇,𞤾)
 with 뵿(𐡁):
  𣜠(泠,𞤾,ࠕ)
 with 뵿(𐡁):
  𣜠(泠,ㅜ,create_parent=ࠕ)
 with 뵿(𐡁):
  𣜠(泠,'')
 𣜠(泠,𞤾)
 pass
def ﲐ():
 泠=𦻃()
 𞢞=𨭹.join(泠,𠹋(5))
 𡇊=𨭹.join(泠,𠹋(5))
 ᙸ=𨭹.join(𡇊,𠹋(3))
 𐢈(ᙸ)
 𐢈(𞢞)
 assert 𨭹.isdir(ᙸ)
 assert 𨭹.isdir(𞢞)
 assert 𨭹.isdir(𡇊)
 𐫆(𧃐)
 𐫆("gibberish")
 𐫆(泠)
 assert not 𨭹.isdir(ᙸ)
 assert not 𨭹.isdir(𞢞)
 assert not 𨭹.isdir(𡇊)
 pass
def ﻐ():
 if 𘉘:
  𢕛=𦻃()
  𢜪=𞢂("test",suffix=".exe",dir=𢕛)
  脃(𧃐)
  脃("does_not_exist")
  脃(𢜪)
  pass
 else:
  脃(𧃐)
def ﱦ():
 泠=𦻃()
 𞢞=𨭹.join(泠,𠹋(5))
 𡇊=𨭹.join(泠,𠹋(5))
 ᙸ=𨭹.join(𡇊,𠹋(3))
 𐢈(ᙸ)
 𐢈(𞢞)
 䍮=𞢂("test",dir=泠)
 𠵃=𞢂("test2",dir=𞢞)
 𐰑=𞢂("test3",dir=ᙸ)
 ﲂ(䍮,懩|𗁇|𪿄)
 ﲂ(𠵃,懩|𗁇|𪿄)
 ﲂ(𐰑,懩|𗁇|𪿄)
 assert 𨭹.isdir(泠)
 assert 𨭹.isdir(ᙸ)
 ﴒ=뙭(泠)
 assert not 𨭹.isdir(ᙸ)
 assert not 𨭹.isdir(𞢞)
def 𤨣():
 泠=𦻃()
 𞢞=𨭹.join(泠,𠹋(5))
 𡇊=𨭹.join(泠,𠹋(5))
 ᙸ=𨭹.join(𡇊,𠹋(3))
 𐢈(ᙸ)
 𐢈(𞢞)
 䍮=𞢂("test",dir=泠)
 𠵃=𞢂("test2",dir=𞢞)
 𐰑=𞢂("test3",dir=ᙸ)
 ﲂ(䍮,懩|𗁇|𪿄)
 ﲂ(𠵃,懩|𗁇|𪿄)
 ﲂ(𐰑,懩|𗁇|𪿄)
 assert 𨭹.isdir(泠)
 assert 𨭹.isdir(ᙸ)
 ﴒ=뙭(泠,recursive=ࠕ)
 assert 𨭹.isdir(ᙸ)
 assert 𨭹.isdir(𞢞)
def 뙜():
 assert[]==𐪏(𧃐)
 assert[]==𐪏("gibberish")
 泠=𦻃()
 𞢞=𨭹.join(泠,𠹋(5))
 𡇊=𨭹.join(泠,𠹋(5))
 ᙸ=𨭹.join(𡇊,𠹋(3))
 𐢈(ᙸ)
 𐢈(𞢞)
 䍮=𞢂("test",dir=泠)
 𠵃=𞢂("test2",dir=𞢞)
 𐰑=𞢂("test3",dir=ᙸ)
 ﴒ=𐪏(泠)
 assert 䍮 in ﴒ
 assert 𠵃 in ﴒ
 assert 𐰑 in ﴒ
 assert ᙸ in ﴒ
 assert 𞢞 in ﴒ
def 𥻒():
 𢕛=__file__
 assert not ݮ(𢕛)
 assert not ݮ(𧃐)
 𐳇=𢕛+"_bad"
 assert not ݮ(𐳇)
def 𐬝():
 泠=𦻃()
 㠨=𪈭(prefix="replace_folder_dest_",dir=泠)
 ﰌ=𪈭(prefix="replace_folder_src_",dir=泠)
 斏=𨭹.join(ﰌ,"src")
 𐢈(斏+"/src_folder1/src_folder2")
 ﲙ(斏,㠨)
 𞺻=𨭹.normpath(㠨+".bak")
 assert not 𨭹.exists(斏)
 assert 𨭹.exists(㠨+"/src_folder1/src_folder2")
 𐤁(ﰌ)
 𐤁(㠨)
 assert not 𨭹.exists(㠨)
 assert not 𨭹.exists(ﰌ)
@𐤋.skipif(not 𘉘,reason='OSx implementation for unsupported characters')
def 뵠():
 𩋈='Test file name ([{~`!@#$%^&*()_+|?><\'"}])?.txt'
 ߏ,㣍=ࢱ(𩋈)
 assert 㣍 is ࡈ
 assert ߏ=='Test file name ([{~`!@#$%^&*()_+?><\'"}])?.txt'
@𐤋.skipif(not 𦗵,reason='Windows implementation for unsupported characters')
def ߜ():
 𩋈='Test file name ([{~`!@#$%^&*()_+|?><\'"}])?.txt'
 ߏ,㣍=ࢱ(𩋈)
 assert 㣍 is ࡈ
 if 𐩸[:3]=="win":
  assert ߏ=='Test file name ([{~`!@#$^&()_+\'}]).txt'
 else:
  assert ߏ=='Test file name ([{~`!@#$%^&()_+\'}]).txt'
def 𫜋():
 𩋈='.filename.txt.'
 ߏ,㣍=ࢱ(𩋈)
 assert 㣍 is ࡈ
 assert ߏ=='filename.txt'
def 𞺭():
 𩋈='filename with 👀 eyes  👀'
 ߏ,㣍=ࢱ(𩋈)
 assert 㣍 is ࡈ
 assert ߏ=='filename with  eyes  '
def ﺱ():
 𩋈='漢語'
 ߏ,㣍=ࢱ(𩋈)
 assert 㣍 is ࠕ
 assert ߏ==𩋈
if __name__=='__main__':
 ﴍ([__file__,'-s','-v'])
# Created by pyminifier (https://github.com/liftoff/pyminifier)
