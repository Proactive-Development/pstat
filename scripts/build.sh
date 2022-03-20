zip -r app_build.zip *
echo '#!/usr/bin/env python3' | cat - app_build.zip > pstat
chmod +x pstat